from optparse import OptionParser, OptionGroup
from HiggsAnalysis.HiggsToTauTau.LimitsConfig import configuration
import os

## set up the option parser
parser = OptionParser(usage="usage: %prog [options]",
                      description="Script to run all macros to create postfit plots. Macros have to be prodiced before hand and are expected to be located in the test directory.")
## direct options
parser.add_option("-a", "--analysis", dest="analysis", default="sm", type="choice", help="Type of analysis (sm or mssm). Lower case is required. [Default: sm]", choices=["sm", "mssm"])
parser.add_option("-p", "--periods", dest="periods", default="7TeV 8TeV", type="string", help="List of run periods for which the datacards are to be copied. [Default: \"7TeV 8TeV\"]")
parser.add_option("-c", "--config", dest="config", default="{CMSSW}/src/HiggsAnalysis/HiggsToTauTau/limits.config".format(CMSSW=os.getenv('CMSSW_BASE')), type="string", help="Configuration to be used. [Default: '']")
## check number of arguments; in case print usage
(options, args) = parser.parse_args()
if len(args) > 0 :
    parser.print_usage()
    exit(1)

#import configuration 
config=configuration(options.analysis, options.config)

log = {
    ("em", "0") : ["false",],
    ("em", "1") : ["false",],
    ("em", "2") : ["false",],
    ("em", "3") : ["false",],
    ("em", "4") : ["false",],
    ("em", "5") : ["false",],
    ("em", "6") : ["false",],
    ("em", "7") : ["false",],
    ("em", "8") : ["false", "true"],
    ("em", "9") : ["false", "true"],
    ("mt", "0") : ["false",], 
    ("mt", "1") : ["false",],
    ("mt", "2") : ["false",],
    ("mt", "3") : ["false",],
    ("mt", "4") : ["false",],
    ("mt", "5") : ["false",],
    ("mt", "6") : ["false",],
    ("mt", "7") : ["false",],
    ("mt", "8") : ["false", "true"],
    ("mt", "9") : ["false", "true"],
    ("et", "0") : ["false" ],
    ("et", "1") : ["false" ],
    ("et", "2") : ["false" ],
    ("et", "3") : ["false" ],
    ("et", "4") : ["false" ],
    ("et", "5") : ["false",],
    ("et", "6") : ["false",],
    ("et", "7") : ["false",],
    ("et", "8") : ["false", "true"],
    ("et", "9") : ["false", "true"],
    ("tt", "0") : ["false",],
    ("tt", "1") : ["false",],
    ("tt", "2") : ["false",],
    ("tt", "8") : ["false", "true"],
    ("tt", "9") : ["false", "true"],
    ("mm", "0") : ["false", "true"],
    ("mm", "1") : ["false", "true"], 
    ("mm", "2") : ["false", "true"],
    ("mm", "3") : ["false", "true"],
    ("mm", "4") : ["false", "true"],
    ("mm", "6") : ["false",],
    ("mm", "7") : ["false",],
    ("mm", "8") : ["false", "true"],
    ("mm", "9") : ["false", "true"],
    ("ee", "0") : ["false", "true"],
    ("ee", "1") : ["false", "true"], 
    ("ee", "2") : ["false", "true"],
    ("ee", "3") : ["false", "true"],
    ("ee", "4") : ["false", "true"],
    }

max = {
    ("em", "0") :  ["-1."],
    ("em", "1") :  ["-1."],
    ("em", "2") :  ["-1."],
    ("em", "3") :  ["-1."],
    ("em", "4") :  ["-1."],
    ("em", "5") :  ["-1."],
    ("em", "6") :  ["-1."],
    ("em", "7") :  ["-1."],
    ("em", "8") :  ["-1.", "-1"],
    ("em", "9") :  ["-1.", "-1"],
    ("mt", "0") :  ["-1."],
    ("mt", "1") :  ["-1."],
    ("mt", "2") :  ["-1."],
    ("mt", "3") :  ["-1."],
    ("mt", "4") :  ["-1."],
    ("mt", "5") :  ["-1."],
    ("mt", "6") :  ["-1."],
    ("mt", "7") :  ["-1."],
    ("mt", "8") :  ["-1.", "-1"],
    ("mt", "9") :  ["-1.", "-1"],
    ("et", "0") :  ["-1."],
    ("et", "1") :  ["-1."],
    ("et", "2") :  ["-1."],
    ("et", "3") :  ["-1."],
    ("et", "4") :  ["-1."],
    ("et", "5") :  ["-1."],
    ("et", "6") :  ["-1."],
    ("et", "7") :  ["-1."],
    ("et", "8") :  ["-1.", "-1"],
    ("et", "9") :  ["-1.", "-1"],
    ("tt", "0") :  ["-1."],
    ("tt", "1") :  ["-1."],
    ("tt", "2") :  ["-1."],
    ("tt", "8") :  ["-1.", "-1"],
    ("tt", "9") :  ["-1.", "-1"],
    ("mm", "0") :  ["-1.", "-1"],
    ("mm", "1") :  ["-1.", "-1"],
    ("mm", "2") :  ["-1.", "-1"],
    ("mm", "3") :  ["-1.", "-1"],
    ("mm", "4") :  ["-1.", "-1"],
    ("mm", "6") :  ["-1."],
    ("mm", "7") :  ["-1."],
    ("mm", "8") :  ["-1.", "-1"],
    ("mm", "9") :  ["-1.", "-1"],
    ("ee", "0") :  ["-1.", "-1"],
    ("ee", "1") :  ["-1.", "-1"],
    ("ee", "2") :  ["-1.", "-1"],
    ("ee", "3") :  ["-1.", "-1"],
    ("ee", "4") :  ["-1.", "-1"],
    }

min = {
    ("em", "0") : ["0."],
    ("em", "1") : ["0."],
    ("em", "2") : ["0."],
    ("em", "3") : ["0."],
    ("em", "4") : ["0."],
    ("em", "5") : ["0."],
    ("em", "6") : ["0."],
    ("em", "7") : ["0."],
    ("em", "8") : ["0.", "3e-2"],
    ("em", "9") : ["0.", "3e-2"],
    ("mt", "0") : ["0."],
    ("mt", "1") : ["0."], 
    ("mt", "2") : ["0."],
    ("mt", "3") : ["0."],
    ("mt", "4") : ["0."],
    ("mt", "5") : ["0."],
    ("mt", "6") : ["0."],
    ("mt", "7") : ["0."],
    ("mt", "8") : ["0.", "1e-2"],
    ("mt", "9") : ["0.", "1e-2"],
    ("et", "0") : ["0."],
    ("et", "1") : ["0."],
    ("et", "2") : ["0."],
    ("et", "3") : ["0."],
    ("et", "4") : ["0."],
    ("et", "5") : ["0."],
    ("et", "6") : ["0."],
    ("et", "7") : ["0."],
    ("et", "8") : ["0.", "1e-2"],
    ("et", "9") : ["0.", "1e-2"],
    ("tt", "0") : ["0."],
    ("tt", "1") : ["0."],
    ("tt", "2") : ["0."],
    ("tt", "8") : ["0.", "3e-1"],
    ("tt", "9") : ["0.", "1e-2"],
    ("mm", "0") : ["0.", "1e-2"],
    ("mm", "1") : ["0.", "1e-2"],
    ("mm", "2") : ["0.", "1e-2"],
    ("mm", "3") : ["0.", "1e-2"],
    ("mm", "4") : ["0.", "1e-2"],
    ("mm", "6") : ["0."],
    ("mm", "7") : ["0."],
    ("mm", "8") : ["0.", "1e-2"],
    ("mm", "9") : ["0.", "1e-2"],
    ("ee", "0") : ["0.", "1e-2"],
    ("ee", "1") : ["0.", "1e-2"],
    ("ee", "2") : ["0.", "1e-2"],
    ("ee", "3") : ["0.", "1e-2"],
    ("ee", "4") : ["0.", "1e-2"],
    }

for chn in config.channels :
    for per in config.periods :
        for cat in config.categories[chn][per] :
            for sca in ["true", "false"] :
                for i in range(len(log[chn,cat])) :
                    if chn == "hbb" :
                        bash_script = "root -l -b -q {CHN}_{CAT}_{PER}.C+\(\"{SCA}\",\"{LOG}\",{MIN},{MAX}\)".format(
                            SCA=sca,
                            LOG=log[(chn,cat)][i],
                            MIN=min[(chn,cat)][i],
                            MAX=max[(chn,cat)][i],
                            CHN=chn,
                            CAT=cat,
                            PER=per
                            )
                    else :
                        bash_script = "root -l -b -q htt_{CHN}_{CAT}_{PER}.C+\(\"{SCA}\",\"{LOG}\",{MIN},{MAX}\)".format(
                            SCA=sca,
                            LOG=log[(chn,cat)][i],
                            MIN=min[(chn,cat)][i],
                            MAX=max[(chn,cat)][i],
                            CHN=chn,
                            CAT=cat,
                            PER=per
                            )
                    os.system(bash_script)
