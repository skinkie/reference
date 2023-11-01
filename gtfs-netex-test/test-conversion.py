class test():
    @staticmethod
    def get_or_none(l: list, i: int):
        if l is None:
            return l
        return l[i]


    def getOperators(self) -> list[Operator]:
        feed_info_sql = """select * from agency;"""
        results = []

        with self.conn.cursor() as cur:
            cur.execute(feed_info_sql)
            df = cur.df()

            agency_ids = df.get('agency_id')
            agency_names = df.get('agency_name')
            agency_timezones = df.get('agency_timezone')
            agency_langs = df.get('agency_lang')
            agency_phones = df.get('agency_phone')
            agency_urls = df.get('agency_url')
            agency_emails = df.get('agency_email')

            for i in range(0, len(agency_ids)):
                operator = Operator(name=MultilingualString(get_or_none(agency_names, i)),
                                    locale=Locale(time_zone=get_or_none(agency_timezones, i),
                                                  languages=LocaleStructure.Languages(language_usage=[
                                                      LanguageUsageStructure(language=get_or_none(agency_langs, i),
                                                                             language_use=[
                                                                                 LanguageUseEnumeration.NORMALLY_USED])])),
                                    customer_service_contact_details=ContactStructure(url=get_or_none(agency_urls, i),
                                                                                      phone=get_or_none(agency_phones, i),
                                                                                      email=get_or_none(agency_emails, i)))
                setIdVersion(operator, self.codespace, get_or_none(agency_ids, i), None)
                results.append(operator)

        return results
