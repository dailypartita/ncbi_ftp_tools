for md5 in *.md5; do
    nohup md5sum -c $md5 > ${md5%.md5}.check 2>&1 &
done
