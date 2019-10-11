"""
The plot utils module contains some useful routines related to plotting.
"""

import matplotlib.patches as mpatches
import numpy as np

def phase_legend(phases):
    """
    Build matplotlib handles for the plot legend.

    Parameters
    ----------
    phases : list
        Names of the phases.

    Returns
    -------
    A tuple containing:
    (1) A list of matplotlib handle objects
    (2) A dict mapping phase names to their RGB color on the plot

    Examples
    --------
    >>> legend_handles, colors = phase_legend(['FCC_A1', 'BCC_A2', 'LIQUID'])
    """
    colorlist = {}
    # colors from HU1SUN, August 5 2018, ordered by igorjrd, issue #97
    # exclude green and red because of their special meaning on the diagram
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ENH: Use better colors in phase_legend()
=======
>>>>>>> ENH:  Use better colors in phase_legend()
=======
>>>>>>> Update installation instructions to include
    colorvalues = [
        '00538A', 'F4C800', 'F13A13', 'C10020', 'D2F300', '53377A', '7BD1EC',
        '232C16', 'FE4262', 'C0DE00', '704AA4', 'FFB300', '176136', '7F180D',
        '93AA00', '2B85EB', 'F6768E', '007D34', '803E75', '4A7C01', 'FF8E00',
        'EC1840', '178D39', 'B32851', '577C23', 'A6BDD7', 'FD522B', '526B2E',
        '90324E', '593315', 'B6A0D4', 'FF6800', 'CEA262', '9A7CC4', '91250B',
        '7B3D0B', 'FF7A5C', 'C01F3D', 'D39336', '817066', '96541F', 'EB9867',
        'B15106', 'EE8548', '97691C', 'DF6B10', '987155', 'C76F32', 'B37347',
    ]
=======
<<<<<<< HEAD
=======
>>>>>>> ENH: Use better colors in phase_legend()
=======
>>>>>>> ENH: Use better colors in phase_legend()
    colorvalues = ['#00538a', '#f4c800', '#f13a13', '#c10020', '#d2f300',
                   '#53377a', '#7bd1ec', '#232c16', '#fe4262', '#c0de00',
                   '#704aa4', '#ffb300', '#176136', '#7f180d', '#93aa00',
                   '#2b85eb', '#f6768e', '#007d34', '#803e75', '#4a7c01',
                   '#ff8e00', '#ec1840', '#178d39', '#b32851', '#577c23',
                   '#a6bdd7', '#fd522b', '#526b2e', '#90324e', '#593315',
                   '#b6a0d4', '#ff6800', '#cea262', '#9a7cc4', '#91250b',
                   '#7b3d0b', '#ff7a5c', '#cea262', '#c01f3d', '#d39336',
                   '#817066', '#96541f', '#eb9867', '#b15106', '#ee8548',
                   '#97691c', '#df6b10', '#987155', '#c76f32', '#b37347']
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ENH: Use better colors in phase_legend()
=======
=======
>>>>>>> ENH:  Use better colors in phase_legend()
    colorvalues = ['00538a', 'f4c800', 'f13a13', 'c10020', 'd2f300',
                   '53377a', '7bd1ec', '232c16', 'fe4262', 'c0de00',
                   '704aa4', 'ffb300', '176136', '7f180d', '93aa00',
                   '2b85eb', 'f6768e', '007d34', '803e75', '4a7c01',
                   'ff8e00', 'ec1840', '178d39', 'b32851', '577c23',
                   'a6bdd7', 'fd522b', '526b2e', '90324e', '593315',
                   'b6a0d4', 'ff6800', 'cea262', '9a7cc4', '91250b',
                   '7b3d0b', 'ff7a5c', 'c01f3d', 'd39336',
                   '817066', '96541f', 'eb9867', 'b15106', 'ee8548',
                   '97691c', 'df6b10', '987155', 'c76f32', 'b37347']
<<<<<<< HEAD
>>>>>>> ENH:  Use better colors in phase_legend()
=======
    colorvalues = [
        '00538A', 'F4C800', 'F13A13', 'C10020', 'D2F300', '53377A', '7BD1EC',
        '232C16', 'FE4262', 'C0DE00', '704AA4', 'FFB300', '176136', '7F180D',
        '93AA00', '2B85EB', 'F6768E', '007D34', '803E75', '4A7C01', 'FF8E00',
        'EC1840', '178D39', 'B32851', '577C23', 'A6BDD7', 'FD522B', '526B2E',
        '90324E', '593315', 'B6A0D4', 'FF6800', 'CEA262', '9A7CC4', '91250B',
        '7B3D0B', 'FF7A5C', 'C01F3D', 'D39336', '817066', '96541F', 'EB9867',
        'B15106', 'EE8548', '97691C', 'DF6B10', '987155', 'C76F32', 'B37347',
    ]
>>>>>>> Update installation instructions to include
=======
>>>>>>> ENH: Use better colors in phase_legend()
=======
>>>>>>> ENH:  Use better colors in phase_legend()
=======
    colorvalues = [
        '00538A', 'F4C800', 'F13A13', 'C10020', 'D2F300', '53377A', '7BD1EC',
        '232C16', 'FE4262', 'C0DE00', '704AA4', 'FFB300', '176136', '7F180D',
        '93AA00', '2B85EB', 'F6768E', '007D34', '803E75', '4A7C01', 'FF8E00',
        'EC1840', '178D39', 'B32851', '577C23', 'A6BDD7', 'FD522B', '526B2E',
        '90324E', '593315', 'B6A0D4', 'FF6800', 'CEA262', '9A7CC4', '91250B',
        '7B3D0B', 'FF7A5C', 'C01F3D', 'D39336', '817066', '96541F', 'EB9867',
        'B15106', 'EE8548', '97691C', 'DF6B10', '987155', 'C76F32', 'B37347',
    ]
>>>>>>> Update installation instructions to include
=======
>>>>>>> ENH: Use better colors in phase_legend()
>>>>>>> ENH: Use better colors in phase_legend()
=======
    colorvalues = ['00538a', 'f4c800', 'f13a13', 'c10020', 'd2f300',
                   '53377a', '7bd1ec', '232c16', 'fe4262', 'c0de00',
                   '704aa4', 'ffb300', '176136', '7f180d', '93aa00',
                   '2b85eb', 'f6768e', '007d34', '803e75', '4a7c01',
                   'ff8e00', 'ec1840', '178d39', 'b32851', '577c23',
                   'a6bdd7', 'fd522b', '526b2e', '90324e', '593315',
                   'b6a0d4', 'ff6800', 'cea262', '9a7cc4', '91250b',
                   '7b3d0b', 'ff7a5c', 'c01f3d', 'd39336',
                   '817066', '96541f', 'eb9867', 'b15106', 'ee8548',
                   '97691c', 'df6b10', '987155', 'c76f32', 'b37347']
>>>>>>> ENH:  Use better colors in phase_legend()
=======
    colorvalues = [
        '00538a', 'f4c800', 'f13a13', 'c10020', 'd2f300', '53377a', '7bd1ec',
        '232c16', 'fe4262', 'c0de00', '704aa4', 'ffb300', '176136', '7f180d',
        '93aa00', '2b85eb', 'f6768e', '007d34', '803e75', '4a7c01', 'ff8e00',
        'ec1840', '178d39', 'b32851', '577c23', 'a6bdd7', 'fd522b', '526b2e',
        '90324e', '593315', 'b6a0d4', 'ff6800', 'cea262', '9a7cc4', '91250b',
        '7b3d0b', 'ff7a5c', 'c01f3d', 'd39336', '817066', '96541f', 'eb9867',
        'b15106', 'ee8548', '97691c', 'df6b10', '987155', 'c76f32', 'b37347'
    ]
>>>>>>> Update installation instructions to include
    mxx = len(colorvalues)
    phasecount = 0
    legend_handles = []
    for phase in phases:
        phase = phase.upper()
        colorlist[phase] = "#"+colorvalues[np.mod(phasecount, mxx)]
        legend_handles.append(mpatches.Patch(color=colorlist[phase], label=phase))
        phasecount = phasecount + 1
    return legend_handles, colorlist
