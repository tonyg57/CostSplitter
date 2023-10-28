# CostSplitter -- Cost Splitter for two or three way scenarios.
This was originally done in Excel but wanted a stand-alone program. When I go on week long motorcycle rides with one or two other riders, we take turns paying for the lodging each night. As each night usually costs a different amount, it can get maddening as to how to evenly share the costs. I found that I just tally up the entire lodging cost and divide it by either by 2 or 3 -- depending on how many us there were. That gives me the even share cost and then that has to be compared against how much each person actually paid over the course of the trip to settle up with each other.  While doing this for just two people is trivial, it gets more complicated when there are three. Of course, there is the assumption that each person stayed an equal number of nights.

I have a Python version of this that needs just a bit more work but the BASIC version is working fine.  I used QB64 which is an enhanced version of MS QuickBasic 4.5 but is able to create console applications suitable for Windows 10.

Note that I do have some default names in there.  Change them to your preference.  I always ride with the same three guys.

Also, I'm including two additional files, in Python, that were created with ChatGPT assistance: Split2.py and Split3.py.  These programs take a dictionary list of motel/city names, the cost of each motel, and then attempts to find the best combination to equitably split the costs to minimize the settlement charges between persons.
