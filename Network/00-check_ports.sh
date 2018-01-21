echo "Scanning TCP ports..."
server="cloud.stenotype.es"
ports=[21,22,443,80,8080]
for port in {1..80} # Improve this point
do
  (echo >/dev/tcp/$server/$port) >/dev/null 2>&1 && echo "TCP $port open." || echo "TCP port $port close."
done
