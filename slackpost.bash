#!/bin/sh
curl -d "text=\`TEST MESSAGE: User $1 starting observation on project $2: $2\`" -d "channel=${ATACHANNEL}" -H "Authorization: Bearer ${ATATOKEN}" -X POST https://slack.com/api/chat.postMessage
echo ""


