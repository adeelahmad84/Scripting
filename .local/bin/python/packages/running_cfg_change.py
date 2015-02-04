#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           running_cfg_change.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Module for working out running/startup configuration sync.
"""

def determine_run_start_sync_state(run_change_sysuptime, start_save_sysuptime):
    '''
    return True if run/start are in sync
    return False if run/start are out of sync (or can't be determined after reload)

    '''

    # No 'wr mem' since last reload
    if start_save_sysuptime == 0:
        return False

    elif start_save_sysuptime >= run_change_sysuptime:
        return True

    return False


def convert_uptime_hours(sys_uptime):
    '''
    sys_uptime is in hundredths of seconds

    returns a float
    '''
    return int(sys_uptime) / 100.0 / 3600.0
