echo $1

cd "$1"

gitlog=`git log --pretty=format:'%H%n%an%n%ai'`

IFS_BAK=$IFS
IFS="
"

counter=0
for line in $gitlog;
do
  if (($counter % 3 == 2));
  then
    #this is guarenteed to run last 
    date=$line
    echo "HASH" $hash
    echo "By" $author
    echo "On" $date
    #git checkout $hash
    #run tests
    python db.py $hash $author $date
  elif (($counter % 3 == 1));
  then
    author=$line
  else 
    hash=$line
  fi
  counter=$((counter+1))
done

IFS=$IFS_BAK
IFS_BAK=
