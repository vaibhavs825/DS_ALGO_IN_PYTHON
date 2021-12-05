def findSongsOld(rideDuration, songDurations):
    # Write your code here
    rideDuration -= 30
    if rideDuration<0:
        return [-1,-1]
    sorted_song_duration = sorted(enumerate(songDurations), key=lambda x:x[1])
    l = 0
    r = len(sorted_song_duration)-1
    max_song_len = 0
    result = [-1,-1]
    while(l<r):
        s1 = sorted_song_duration[l][1]
        s2 = sorted_song_duration[r][1]
        if s1+s2 == rideDuration:
            if s1 > max_song_len or s2 > max_song_len:
                result = sorted([sorted_song_duration[l][0],sorted_song_duration[r][0]])
                max_song_len = max(s1,s2)
            r -= 1
            l += 1
        elif s1+s2>rideDuration:
            r -= 1
        else:
            l += 1

    return result

print(findSongs(250, [5,100,180,40,120,10]))


def findSongs(rideDuration, songDurations):
    # Write your code here
    rideDuration -= 30
    if rideDuration<=0:
        return [-1,-1]
    map_songs = {}
    longest = 0
    result = [-1,-1]
    for idx,i in enumerate(songDurations):
        complement = rideDuration-i
        if (i>longest or complement>longest) and (complement in map_songs):
            result = [map_songs[complement],idx]
            longest = max(i,complement)
        map_songs[i] = idx
    return result