from ghapi.core import GhApi
api = GhApi(owner='tensorflow', repo='tensorflow', token="${{ secrets.GITHUB_TOKEN }}")
api.delete_branch('new-branch')
