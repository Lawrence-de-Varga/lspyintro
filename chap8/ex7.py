info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh' 

info = info.split(':')
info = '+'.join(info)

print(info)


info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh' 

info = info.replace(':', '+')

print(info)
