##### Generate Random data pattern

Sample data pattern

```
1863.1888.3176.F5nsSQZ
4036.7711.1758.ZZVGQhs
2038.3104.2515.YX8PHVn
1845.2646.1782.BW1qqdW
2144.1845.2998.yaA0Bt1
```


Script to generate data file
```
while (true) do echo ${RANDOM:0:4}.${RANDOM:0:4}.${RANDOM:0:4}.$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c7) >> data.txt ; done
```


