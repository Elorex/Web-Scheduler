## HEAT Templates originally written by Carl Janzen
## Source: git@cisgitlab.ufv.ca:201901COMP351AB1s00/heat-templates.git 

#!/usr/bin/env bash
# exit if KEYS_URL is blank
[ -z "$KEYS_URL" ] && exit 0

# fetch new copy of public keys
rm -f /tmp/fetched_keys || exit 1
touch /tmp/fetched_keys || exit 1
chmod 0600 /tmp/fetched_keys || exit 1
curl $KEYS_URL > /tmp/fetched_keys

# update every authorized_keys file
cd /home
for fn in * ; do
[ -e "${fn}/.ssh/authorized_keys" ] && {
	rm -f /tmp/$$authorized_keys
	touch /tmp/$$authorized_keys
	chmod 0600 /tmp/$$authorized_keys
	cat "${fn}/.ssh/authorized_keys" > /tmp/$$authorized_keys
	cat /tmp/fetched_keys >> /tmp/$$authorized_keys
	sort -u /tmp/$$authorized_keys > "${fn}/.ssh/authorized_keys"
    rm -f /tmp/$$authorized_keys
}
rm -f /tmp/fetched_keys
done
