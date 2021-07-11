dtlz = '2'

minVals = [99999, 99999, 99999]

for x in range(1,11):
  minVals = [99999, 99999, 99999]
  f = open(f"../../output/DTLZ{dtlz}T/GlobalResults_DTLZ{dtlz}_10D_DM{x}.txt", "r")
  cont = 0
  contSaved = 0
  for i in f:
    cont+=1
    actualVals = i.rstrip().replace('(', '').replace(')', '').split(', ')
    if int(actualVals[0]) == 0:
      if int(actualVals[1]) == 0:
        if int(actualVals[2]) < minVals[2]:
          minVals[0] = int(actualVals[0]);
          minVals[1] = int(actualVals[1]);
          minVals[2] = int(actualVals[2]);
          contSaved = cont
  
  f.close()

  o = open(f"../../output/DTLZ{dtlz}T/Globalwithoutduplicates{dtlz}.txt","r")
  all_lines = o.readlines()

  dmFile = open(f"../../output/DTLZ{dtlz}T/DM{x}T.txt", "a")
  dmFile.write(all_lines[contSaved - 1]) 
  dmFile.close()

  o.close()