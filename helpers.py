import numpy as np


def eseries(series='E12', minimal=0.01, maximal=300):
    assert minimal > 10**-10
    assert maximal < 10**20
    minimal *= 0.99999
    maximal *= 1.00001

    ereihen = {
        'E6' : np.array([100,150,220,330,470,680]),
        'E12': np.array([100,120,150,180,220,270,330,390,470,560,680,820]),
        'E24': np.array([100,110,120,130,150,160,180,200,220,240,270,300,330,360,390,430,470,510,560,620,680,750,820,910]),
        'E48': np.array([100,105,110,115,121,127,133,140,147,154,162,169,178,187,196,205,
        215,226,237,249,261,274,287,301,316,332,348,365,383,402,422,442,464,487,511,536,562,590,619,649,681,715,750,787,825,866,909,953]),
        'E96': np.array([100,102,105,107,110,113,115,118,121,124,127,130,133,137,140,143,147,150,154,158,162,165,169,174,
        178,182,187,191,196,200,205,210,215,221,226,232,237,243,249,255,261,267,274,280,287,294,301,309,
        316,324,332,340,348,357,365,374,383,392,402,412,422,432,442,453,464,475,487,499,511,523,536,549,
        562,576,590,604,619,634,649,665,681,698,715,732,750,768,787,806,825,845,866,887,909,931,953,976]),
        'E192': np.array([100,101,102,104,105,106,107,109,110,111,113,114,115,117,118,120,121,123,124,126,127,129,130,132,
        133,135,137,138,140,142,143,145,147,149,150,152,154,156,158,160,162,164,165,167,169,172,174,176,
        178,180,182,184,187,189,191,193,196,198,200,203,205,208,210,213,215,218,221,223,226,229,232,234,
        237,240,243,246,249,252,255,258,261,264,267,271,274,277,280,284,287,291,294,298,301,305,309,312,
        316,320,324,328,332,336,340,344,348,352,357,361,365,370,374,379,383,388,392,397,402,407,412,417,
        422,427,432,437,442,448,453,459,464,470,475,481,487,493,499,505,511,517,523,530,536,542,549,556,
        562,569,576,583,590,597,604,612,619,626,634,642,649,657,665,673,681,690,698,706,715,723,732,741,
        750,759,768,777,787,796,806,816,825,835,845,856,866,876,887,898,909,920,931,942,953,965,976,988])
    }
    serie = ereihen[series]
    valuelist = np.array([])

    dekade_min = int(round(np.log10(minimal)-0.5))
    dekade_max = int(round(np.log10(maximal)+0.5))
    for decade in range(dekade_min, dekade_max):
        for value in serie:
            entry = value * 10**decade / 100.0
            if minimal <= entry <= maximal:
                valuelist = np.append(valuelist, entry)
    #print(valuelist)
    return(valuelist)

def get_list_measurements(frequencies_Hz):
    minimal_duration_s = 0.1
    maximal_duration_s = 150.0
    periods_sine_optimal = 5.0
    list_measurements = list()
    for frequency_Hz in frequencies_Hz:
        duration_s = 1.0 / frequency_Hz * periods_sine_optimal
        if duration_s > maximal_duration_s:
            duration_s = maximal_duration_s
        if duration_s < minimal_duration_s:
            duration_s = minimal_duration_s
        list_measurements.append( dict(frequency_Hz=frequency_Hz, duration_s=duration_s))
    # print(list_measurements)
    return list_measurements

if __name__ == '__main__':
    frequencies_Hz = eseries(series = 'E12', minimal = 0.01, maximal = 300)
    get_list_measurements(frequencies_Hz)
