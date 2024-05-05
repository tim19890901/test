from git import Repo

repo_url = "https://github.com/tim19890901/test.git"

repo = Repo.clone_from(repo_url, "C:\\Users\\User\\Documents\\pygit\\",branch='test')

print({repo})