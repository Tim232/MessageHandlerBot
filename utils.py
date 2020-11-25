import config

def is_owner(ctx):
    if ctx.author.id in config.owners:
        return True
    return False
