from bolao_bet.models import UserBet, UserGpPoints, UserTotalPoints
from django.contrib.auth.models import User
from django.utils import timezone
import bolao_bet.views


def process_bet_core(gp):
    gp.processed = False
    gp.save()
    
    for user in User.objects.filter(is_active=True):
        
        if UserBet.objects.filter(user=user, GPrix=gp).exists():
            bet = UserBet.objects.filter(user=user, GPrix=gp).latest('date')
        
        else:
            bet = UserBet(user=user, GPrix=gp)
            
            if gp.race_number > 1.5:
                
                if UserBet.objects.filter(user=user, GPrix__year=gp.year,
                        GPrix__race_number=gp.race_number - 1).exists():
                    previous_bet = UserBet.objects.filter(user=user, GPrix__year=gp.year,
                        GPrix__race_number=gp.race_number - 1).latest(
                        'date')
                    
                    bet = UserBet(user=user, GPrix=gp, date=timezone.now())
                    bet.pole = previous_bet.pole
                    bet.p1 = previous_bet.p1
                    bet.p2 = previous_bet.p2
                    bet.p3 = previous_bet.p3
                    bet.p4 = previous_bet.p4
                    bet.p5 = previous_bet.p5
                    bet.p6 = previous_bet.p6
                    bet.p7 = previous_bet.p7
                    bet.p8 = previous_bet.p8
                    bet.p9 = previous_bet.p9
                    bet.p10 = previous_bet.p10
                    
                    bet.repeated = True
                    
                    bet.save()
                
                else:
                    bet.valid = False
                    bet.save()
            else:
                bet.valid = False
                bet.save()
        
        if bet.valid:
            
            # repost bet
            bet.hidden = False
            bet.save()
            bolao_bet.views.make_repost(bet.pk)
            
            # Calculate GP points for current user
            if UserGpPoints.objects.filter(user=user, GPrix=gp).exists():
                new_points = UserGpPoints.objects.filter(user=user, GPrix=gp)
                new_points = new_points[0]
            
            else:
                new_points = UserGpPoints(user=user, GPrix=gp)
            
            new_points.points = gp_points_pole(bet.pole, gp)
            new_points.points += gp_points_position(1, bet.p1, gp)
            new_points.points += gp_points_position(2, bet.p2, gp)
            new_points.points += gp_points_position(3, bet.p3, gp)
            new_points.points += gp_points_position(4, bet.p4, gp)
            new_points.points += gp_points_position(5, bet.p5, gp)
            new_points.points += gp_points_position(6, bet.p6, gp)
            new_points.points += gp_points_position(7, bet.p7, gp)
            new_points.points += gp_points_position(8, bet.p8, gp)
            new_points.points += gp_points_position(9, bet.p9, gp)
            new_points.points += gp_points_position(10, bet.p10, gp)
            
            if gp.double_points:
                new_points.points *= 2
            
            # import pdb;
            # pdb.set_trace()
            
            new_points.save()
        
        else:
            
            if UserGpPoints.objects.filter(user=user, GPrix=gp).exists():
                new_points = UserGpPoints.objects.filter(user=user, GPrix=gp)
            
            else:
                new_points = UserGpPoints(user=user, GPrix=gp)
            
            new_points.points = 0
            new_points.save()
        
        if UserTotalPoints.objects.filter(user=user, GPrix=gp).exists():
            total_points = UserTotalPoints.objects.filter(user=user, GPrix=gp)
            total_points = total_points[0]
        else:
            total_points = UserTotalPoints(user=user, GPrix=gp)
        
        if gp.race_number > 1.5:
            
            if UserTotalPoints.objects.filter(user=user, GPrix__year=gp.year,
                    GPrix__race_number=gp.race_number - 1).exists():
                previous_total_points = UserTotalPoints.objects.filter(user=user, GPrix__year=gp.year,
                    GPrix__race_number=gp.race_number - 1)
                previous_total_points = previous_total_points[0]
            
            else:
                previous_total_points.points = 0
        
        else:
            previous_total_points.points = 0
        
        total_points.points = previous_total_points.points + new_points.points
        total_points.save()
        
    gp.processed = True
    gp.save()


def gp_points_position(position, bet_p, gp):
    points = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
    bonus = 5
    
    gp_pos = 0
    
    gp_pos = (bet_p == gp.p1) * 1
    gp_pos += (bet_p == gp.p2) * 2
    gp_pos += (bet_p == gp.p3) * 3
    gp_pos += (bet_p == gp.p4) * 4
    gp_pos += (bet_p == gp.p5) * 5
    gp_pos += (bet_p == gp.p6) * 6
    gp_pos += (bet_p == gp.p7) * 7
    gp_pos += (bet_p == gp.p8) * 8
    gp_pos += (bet_p == gp.p9) * 9
    gp_pos += (bet_p == gp.p10) * 10
    
    if gp_pos < 0.5:
        gp_pos = 22
    
    if (position + abs(gp_pos - position)) > 10:
        result = 0
    
    else:
        
        result = points[(position + abs(gp_pos - position))]
        
        if abs(gp_pos - position) == 0:
            result += bonus
    
    return result


def gp_points_pole(bet_pole, gp):
    if bet_pole == gp.pole:
        return 12
    else:
        return 0
