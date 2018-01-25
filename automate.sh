#!/usr/bin/env bash
function refresh_link() {
    echo "refresh link"
    for f in $(find . -name README.org); do
        dirname=$(basename $(dirname $f))
        if ! grep "brain.dennyzhang.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update blog url for $f"
            sed -ie "s/Blog link: http:\/\/brain.dennyzhang.com\/.*/Blog link: http:\/\/brain.dennyzhang.com\/$dirname/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "tree\/master.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update GitHub url for $f"
            sed -ie "s/tree\/master\/.*/tree\/master\/$dirname][challenges-leetcode-interesting]]/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "leetcode.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update Leetcode url for $f"            
            sed -ie "s/https:\/\/leetcode.com\/problems\/.*/https:\/\/leetcode.com\/problems\/$dirname\/description\/][leetcode.com]]/g" $f
            rm -rf $dirname/README.orge
        fi
    done
}

function refresh_md() {
    echo "Use emacs to refresh README.md"
    for f in $(find . -name README.org); do
        echo "Update $f"
        dirname=$(basename $(dirname $f))
        cd $dirname
        /Applications/Emacs.app/Contents/MacOS/Emacs-x86_64-10_9 --batch -l ../update_md.el
        cd ..
    done
}

cd .

action=${1?}
case "$action" in 
    refresh_link)
        refresh_link
        ;;
    refresh_md)
        refresh_md
        ;;
        *) 
            echo "no matched action. Supported: refresh_link|refresh_md"
            ;;
esac
