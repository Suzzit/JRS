# Git Worktree Setup
echo "Setting Up..."

git fetch

gitBranches=("front" "back")

for branch in ${gitBranches[@]}; do
    echo "Setting up branch... $branch"
    git checkout $branch
    git switch master
    git worktree add $branch
done