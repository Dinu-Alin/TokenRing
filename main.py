from Token import Token
from itertools import cycle
from ipaddress import ip_address as ip
import logging


def main():
    token = Token()

    logging.basicConfig()

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    ring_routes = []
    unique_ring = set()

    pc_number = int(input("Please enter number of computers: "))
    if pc_number == 0:
        return False

    for index in range(pc_number):
        try:
            curr_ip = input(f"Enter ip number {index + 1}: ")
            curr_ip = ip(curr_ip)
            ring_routes.append(curr_ip)
            if unique_ring.__contains__(curr_ip):
                print(f"Error, ip {curr_ip} is not unique!")
                return False
            else:
                unique_ring.add(curr_ip)
        except:
            print(f"Error, ip {index + 1} is invalid!")
            return False

    while True:
        print(ring_routes)
        print("Number of ip's:" + str(len(ring_routes)))

        message = input("Please enter message: ")
        # pool = cycle(list())
        token.sent_message = message

        user_response_source = int(input("Select source: "))
        user_response_target = int(input("Select target: "))

        if 1 > user_response_target or user_response_target > pc_number or 1 > user_response_source or\
                user_response_source > pc_number:
            print("Error, out of index!")
            return False

        if user_response_target == user_response_source:
            print("Source is the same as target!")
            return False

        token.IP_source = ring_routes[user_response_source - 1]
        token.IP_target = ring_routes[user_response_target - 1]

        user_response = input("Default direction is clockwise. Do you want to change?(y/n) ")

        if user_response == 'y':
            ring_routes.reverse()

        ring_cycle = cycle(ring_routes)
        token.is_free = False

        current_item = None
        while current_item != token.IP_source:
            current_item = next(ring_cycle)
        # print(token)
        while current_item != token.IP_target:
            token.history.append(current_item)
            print(f"PC {current_item}: " + token.__str__())
            current_item = next(ring_cycle)
        else:
            token.history.append(current_item)
            token.finish_line = True
            print(f"PC {current_item}: " + token.__str__())
            print("Messsage printed: " + token.sent_message)
            current_item = next(ring_cycle)

        while current_item != token.IP_source:
            token.history.append(current_item)
            print(f"PC {current_item}: " + token.__str__())
            current_item = next(ring_cycle)
        else:
            token.free()
            print(f"PC {current_item}: " + token.__str__())

        user_response = input("Do you want to sent another message?(y/n) ")
        if user_response != 'y':
            return False


if __name__ == '__main__':
    main()
    # try:
    #     ana = ip("012.22.999.22")
    # except:
    #    print("Error")
    # main()
