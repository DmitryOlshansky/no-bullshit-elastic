BEGIN {
	CNT = 0
}

/^[0-9-]+\s*[0-9:.]+/ {
	CNT += 1
}

END {
	print CNT
}
