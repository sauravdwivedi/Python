"""Mark and Jane are very happy after having their first child. Their son
loves toys, so Mark wants to buy some. There are a number of different toys
lying in front of him, tagged with their prices. Mark has only a certain
amount to spend, and he wants to maximize the number of toys he buys with
this money. Given a list of toy prices and an amount to spend, determine the
maximum number of gifts he can buy.

Note. Each toy can be purchased only once.

Example:

prices = [1,2,3,4]
k = 7

The budget is 7 units of currency. He can buy items that cost [1, 2, 3] for
6, or [3, 4] for 7 units. The maximum is 3 items."""

def mark_and_toys(prices, k):
    """Method to return maximum number of gifts for a given budget"""
    prices = sorted(prices)
    n = len(prices)
    len_list = []
    sub_list = [0]
    i = 1
    while sum(sub_list) <= k:
        len_list.append(len(sub_list))
        sub_list = prices[:i]
        i = i + 1
            
    return max(len_list)
    
if __name__ == '__main__':
    input_file = 'MarkandToys_input.txt'
    try:
        with open(input_file) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File {input_file} is not found!")
    else:
        line_one = list(map(int, lines[0].rstrip().split()))
        prices = list(map(int, lines[1].rstrip().split()))
        n = line_one[0]
        k = line_one[1]
    with open('MarkandToys_output.txt', 'w') as f:
        f.write(f"Max number of gifts: {mark_and_toys(prices, k)}")
    print(f"Output saved in file 'MarkandToys_output.txt'")
