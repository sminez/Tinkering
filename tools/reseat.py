'''Given a class list and a list of ban sets this script
   returns a new seating plan for an 8 table classroom with
   4 pupils per table maximum.
   
   ASSUMPTIONS::
      You are aiming for 8 tables of 4
      -> If this doesn't hold or the number of pupils is
         less than 32 then the program will default to tables
         of 3 once there are 9 pupils left to sit.
      Each name in the class list is unique
      -> If not, make them unique using surnames!
'''

from random import shuffle
from time import time
from itertools import combinations

y10 = ['Tim', 'Bob', 'Sally', 'Jane', 'Ermintrude']

ban10 = [{'Tim', 'Ermintrude'}]


def filter_for_bans(candidates, bans):
    '''
    Input  -> candidates:: list of sets representing 4 pupil groups
              bans::       list of sets of pupils [variable length]
    Output -> c::          a single set that does not contain banned pupil groupings
    '''
    after = []
    ban_count = 0
    total = 0
    for c in candidates:
        banned = False
        for b in bans:
            if len(set(c).intersection(b)) > 1:
                banned = True
        if not banned:
            yield c


def create_plan(candidates, bans, class_names):
    '''
    Input  -> candidates::    list of sets representing 4 pupil tables
              match::         preferred matchings
    Output -> seating_plan:: list of potential 8 4 pupil tables
    '''
    new_plan = []
    accounted_for = set()
    # -- We shuffle the candidate list so that each run of the program gives
    # -- a new solution (possibly...)
    for c in candidates:
        if set(c).intersection(accounted_for) == set():
            new_plan.append(c)
            accounted_for = accounted_for.union(c)
            left_over = set(class_names).difference(accounted_for)
            if len(new_plan) == 8:
                return False, new_plan
            elif len(left_over) <= 9:
                break
    left_to_place = ', '.join(list(left_over))
    print('>>> {} tables filled: now trying to place {}'.format(len(new_plan), left_to_place))
    for c in candidates:
        options = combinations(c, 3)
        for op in options:
            if set(op).intersection(accounted_for) == set():
                new_plan.append(op)
                accounted_for = accounted_for.union(op)
                left_over = set(class_names).difference(accounted_for)
                left_to_place = ', '.join(list(left_over))
                print('>>> {} tables filled: now trying to place {}'.format(len(new_plan), left_to_place))
                if len(new_plan) == 8:
                    return False, new_plan
                elif len(left_over) < 3:
                    break
    # -- If we get to here then we have exhaused our candidate pool due to
    # -- the choices made earlier
    print('Failure:: managed to sit {} tables.'.format(len(new_plan)))
    return True, candidates

def reseat(class_list, bans):
    start = time()
    running = True
    while running:
        # First find all possible 4 seat groupings
        print('Filtering candidate tables...')
        shuffle(class_list)
        #candidates = ([a,b,c,d] for a in  class_list for b in class_list for c in class_list for d in class_list if len({a,b,c,d})==4)
        candidates = combinations(class_list, 4)
        # Now remove any that are on the ban list
        print('Applying restrictions...')
        after_ban = filter_for_bans(candidates, bans)
        # -- Now to create the seating plan
        print('Creating seating plan...')
        #running = True
        # -- If the pass is unsuccessful then we shuffle the input and try again
        #while running:
        running, after_ban = create_plan(after_ban, bans, class_list)
    stop = time() - start
    print('\nSolution found: here is your seating plan ->\n')
    for table in after_ban:
        print(table)
    print('\n--> Finding the solution took {0:.5f}'.format(stop))
    return after_ban


if __name__ == '__main__':
    plan = reseat(y10, ban10)
