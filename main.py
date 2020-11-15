import os
import csv

election_csv = os.path.join("Resources", "PyPoll_Resources_election_data.csv")
#Read in the CSV file:
with open (election_csv) as file_object:
    csvreader = csv.reader(file_object, delimiter=",")
    #print(type(csvreader))
    header = next(csvreader)
    print(f'{header}')
    
    #Initialize variables:
    ids = []
    candidates=[]
    counties = []
    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    OTooley_vote = 0

    for row in csvreader:
        id = row[0]
        county = row[1]
        candidate = row[2]
        
        if county not in counties:
            counties.append(county)
        if candidate not in candidates:
            candidates.append(candidate)
        ids.append(id)
        if row[2] == "Khan":
            Khan_vote += 1
        if row[2] == "Correy":
            Correy_vote += 1
        if row[2] == "Li":
            Li_vote += 1
        if row[2] == "O\'Tooley":
            OTooley_vote +=1 

    total_votes_cast = int(len(ids))
    Khan_pcnt = round(((Khan_vote) /total_votes_cast) * 100, 1)
    Correy_pcnt = round(((Correy_vote) /total_votes_cast) * 100, 1)
    Li_pcnt = round(((Li_vote) /total_votes_cast) * 100, 1)
    OTooley_pcnt = round(((OTooley_vote) /total_votes_cast) * 100, 1)
    vote_amts = [Khan_vote, Correy_vote, Li_vote, OTooley_vote]
    winner_votes = max(vote_amts)
    
    print(f'\n+ + + + + + + + + + + +\nElection Results\n+ + + + + + + + + + + +\n')
    print(f'In total there were {total_votes_cast} votes cast in this election.\n\n+ + + + + + + + + + + + + + \n')
    print(f'The candidates included {candidates}\n')
    print(f'Counties casting votes included {counties}\n')
    
    
    # zip candidate and vote amount lists together into a new dictionary:
    dictionary = dict(zip(candidates, vote_amts))
    
    for key, value in dictionary.items():
        if value == 661583:
            # print(key)
            print(f'\n\tThe winner, {key}, received {winner_votes} votes, which is {Khan_pcnt}% of the total votes.\n')     
    
    print(f'\tCorrey received {Correy_vote} votes, which is {Correy_pcnt}% of the total.\n')
    print(f'\tLi received {Li_vote} votes, which accounts for {Li_pcnt}% of the total.\n')
    print(f'\tO\'Tooley received {OTooley_vote} votes, which represents {OTooley_pcnt}% of the total.\n')

#Write summary to a new file:
with open("PyPoll_Results.txt.", 'w') as text:
    text.write(f'\n+ + + + + + + + + + + +\nElection Results\n+ + + + + + + + + + + +\n')
    text.write(f'\nWINNER: {candidates[0]}\n\n')
    text.write(f'In total there were {total_votes_cast} votes cast in this election.\n\n')
    text.write(f'The candidates included {candidates}\n')
    text.write(f'Counties casting votes included {counties}\n\n')
    text.write(f'Khan received {Khan_pcnt}% of the total vote ({Khan_vote})\n')
    text.write(f'Correy received {Correy_pcnt}% of the total vote ({Correy_vote})\n')
    text.write(f'Li received {Li_pcnt}% of the total vote ({Li_vote})\n')
    text.write(f'O\'Tooley received {OTooley_pcnt}% of the total vote ({OTooley_vote})\n')
    