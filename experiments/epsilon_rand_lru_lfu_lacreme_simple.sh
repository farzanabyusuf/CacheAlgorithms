#!/bin/bash


CACHE_SIZE=0.2
FILES=(epsilon_rand_lru_lfu.txt epsilon_rand_lfu_lru.txt)
ALGORITHMS=(lru lfu arc lacreme_simple)
BLOCKSIZE=1

for ((i=0;i<${#FILES[@]};++i)); do
    python ../run.py "${CACHE_SIZE}" "${FILES[i]}" "${BLOCKSIZE}" "${ALGORITHMS[@]}"
done
