for f in demos/*.dem;
  do demoinfogo "$f" | awk -f shots.awk >> shots.txt
done;
