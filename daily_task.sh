#daily task scheduler
current_date=$(date +'%d%m%Y')
echo "commit date: $current_date" >> commit_log.txt
git add .
git commit -m "$current_date"
git push

