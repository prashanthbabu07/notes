DEV

dev -branch (commit - 0)


d1 - c0
d2 - c0
d3 - c0
d4 - c0


d1 - f1 - commit/pr on day 1
    merge f1 to dev on day 2 - c1

d2 - f2 - coomand/pr on day 3
    if d2 did not rebase then missing dev commint in f2.
    PR will be rejected
    rebase dev into f2 and then create PR for f2
    c0 - c1 - c2


    squash merge the feature branch - 
        (f2 - t1, t2, t3, t4....)

    t1 to t1 would be as aif a single f2 commit and then merge to dev.????


    





