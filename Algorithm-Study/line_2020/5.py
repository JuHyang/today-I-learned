def solution(cards):
    answer = 0

    index = 0
    while index <= len(cards) - 4:
        user = [cards[index], cards[index + 2]]
        for i in range(2):
            user[i] = min(10, user[i])

        user.sort()

        if user[0] == 1 and user[1] >= 6:
            user[0] = 11

        dealer = [cards[index + 1], cards[index + 3]]
        for i in range(2):
            dealer[i] = min(10, dealer[i])
        if sum(user) == 21:
            if sum(dealer) != 21:
                answer += 3

            index += 4
            continue

        index += 4

        if dealer[1] == 1 or dealer[1] >= 7:
            while True:
                if index >= len(cards):
                    break
                i = index

                userSum = sum(user)
                if userSum < 17:
                    index += 1
                    if cards[i] == 1:
                        if userSum >= 6:
                            user.append(11)
                        else:
                            user.append(1)
                    elif cards[i] > 10:
                        user.append(10)
                    else:
                        user.append(cards[i])
                else:
                    break
        elif dealer[1] == 2 or dealer[1] == 3:
            while True:
                if index >= len(cards):
                    break
                i = index

                userSum = sum(user)
                if userSum < 12:
                    index += 1
                    if cards[i] == 1:
                        if userSum >= 6:
                            user.append(11)
                        else:
                            user.append(1)
                    elif cards[i] > 10:
                        user.append(10)
                    else:
                        user.append(cards[i])
                else:
                    break

        if sum(user) > 21:
            answer -= 2
            index += 1
            continue

        dealer.sort()

        if dealer[0] == 1 and dealer[1] >= 6:
            dealer[0] = 11

        while True:
            if index >= len(cards):
                break
            i = index

            dealerSum = sum(dealer)
            if dealerSum < 17:
                index += 1
                if cards[i] == 1:
                    if dealerSum >= 6:
                        dealer.append(11)
                    else:
                        dealer.append(1)
                elif cards[i] > 10:
                    dealer.append(10)
                else:
                    dealer.append(cards[i])
            else:
                break

        if sum(dealer) < 18:
            break

        elif sum(dealer) > 21:
            answer += 2
            index += 1

        elif sum(dealer) == sum(user):
            index += 1
        elif 21 - sum(dealer) > 21 - sum(user):
            answer += 2
            index += 1
        elif 21 - sum(dealer) < 21 - sum(user):
            answer -= 2
            index += 1

    return answer
