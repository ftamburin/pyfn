# XP\#043

open-sesame on FN 1.5 FT with MXPOST

### Test scores
| P | R | F1 |
| --- | --- | --- |
| 59.7 | 59.4 | 59.5 |


### Splits generation
```
pyfn convert \
  --from fnxml \
  --to bios \
  --source /path/to/fndata-1.5-with-dev \
  --target /path/to/experiments/xp_043/data \
  --splits train \
  --output_sentences \
  --filter overlap_fes
```

### Data preparation
```
./prepare.sh -x 043 -p open-sesame -s test -f /path/to/fndata-1.5-with-dev
```

### Preprocessing
```
./preprocess.sh -x 043 -t mxpost -p open-sesame -v
```

### Training
```
./open-sesame.sh -m train -x 043
```

### Decoding
```
./open-sesame.sh -m decode -x 043 -s test
```

### Scoring
```
./score.sh -x 043 -p open-sesame -s test -f gold
```
