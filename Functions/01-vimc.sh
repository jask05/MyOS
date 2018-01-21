function vimc(){
    if [ -f "$1" ]; then
        cp -fp $1 $1_`date +%Y%m%d%H%M%S`
        vim $1
    else
        echo "File \"$1\" does not exist."
    fi
}

export vimc
