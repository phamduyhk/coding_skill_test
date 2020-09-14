# coding: utf-8

def binary_search(card_list, card):
    low = 0
    high = len(card_list) - 1
    print(high)
    while low <= high:
        mid = (low + high) // 2
        #print(mid)
        #print(card_list[mid])
        if card_list[mid] == card:
            print("{0}番目に{1}はあります".format(mid,card))
            return
        elif card_list[mid] < card:
            low = mid + 1
        else:
            high = mid - 1
    return

if __name__ == '__main__':
    heart_cards = [1,2,4,5,6,8,9,10,12,13]
    heart_eight = 8
    binary_search(heart_cards, heart_eight)