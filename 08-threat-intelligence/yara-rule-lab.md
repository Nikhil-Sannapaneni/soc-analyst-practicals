# YARA Rule Lab

## Objective

Learn the structure of a defensive YARA rule using a harmless synthetic sample.

```yara
rule Demo_Synthetic_Indicator
{
    meta:
        description = "Training example only"
        author = "SOC lab"

    strings:
        $marker = "TRAINING_SAMPLE_MARKER"

    condition:
        $marker
}
```

## Rule Design

- Use distinctive strings carefully.
- Avoid overly broad conditions.
- Test against known benign samples.
- Record false positives.
- Version-control rule changes.

Only scan files you are authorised to analyse.
