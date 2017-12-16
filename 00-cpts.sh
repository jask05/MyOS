function cpts(){
    if [ ! -z "$2" ]; then
        if [ -d "$2" ]; then
            cp -rvfp $1 "$2$1_`date +%Y%m%d%H%M%S`"
        else
           echo "Dir \"$2\" does not exist."
        fi
  else
      echo "Empty directory parameter."
  fi
}

export cpts
