#! /bin/sh

I18NDOMAIN="collective.prettydate"

# Synchronise the templates and scripts with the .pot.
# All on one line normally:
i18ndude rebuild-pot --pot src/collective/prettydate/locales/${I18NDOMAIN}.pot \
    --create ${I18NDOMAIN} \
   src/collective/prettydate

# Synchronise the resulting .pot with all .po files
for po in src/collective/prettydate/locales/*/LC_MESSAGES/${I18NDOMAIN}.po; do
    i18ndude sync --pot src/collective/prettydate/locales/${I18NDOMAIN}.pot $po
done
