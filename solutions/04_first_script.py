#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:00:45 2016

@author: proto
"""

def add_track(track_info):
    """Add a single track with name, album, artist, duration."""
    return {
        'track': track_info[0],
        'artist': track_info[1],
        'album': track_info[2],
        'duration': track_info[3]
    }

def parse_data(csv):
    """Parse CSV file into a list of track objects."""
    playlist = []
    with open(csv) as doc:
        for line in doc:
            track = line.split(',')
            playlist.append(add_track(track))
    if playlist[0]['artist'] == ' Artist Name':
        del playlist[0]  # remove first object which contains row names!
    return playlist

def count_tracks(playlist):
    """Return the total number of tracks."""
    return len(playlist)

def list_artists(playlist):
    """Return a list of all unique artists."""
    return set([p['artist'] for p in playlist])
    
def list_tracks(playlist):
    return [t['track'] for t in playlist]

def find_longest_track(playlist):
    """Return the track with the highest duration."""
    return max([int(t['duration'].strip()) for t in playlist])
        
    
# Tests

def test(actual, expected):
    """Always test your work!"""
    if actual == expected:
        result = '==> \u2714 Pass'
    else:
        result = '==> \u2718 Fail'
    print("{0} - Actual: {1}, Expected: {2}".format(result, actual, expected))

def run_tests():
    """Test runner."""
    expected_parse = [{'track': 'test song', 'artist': 'test artist', 'album': 'test album', 'duration': '1000'}]
    test_playlist = parse_data('test_fixture.csv')
    
    print("\n\n")
    test(parse_data('test_fixture.csv'), expected_parse)
    test(count_tracks(test_playlist), 1)
    test(list_artists(test_playlist), ['test artist'])
    test(find_longest_track(test_playlist), 1000)
    
run_tests()
