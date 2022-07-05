import pytest
import logging

LOGGER = logging.getLogger(__name__)

@pytest.mark.usefixtures("search_page_fixture")
class Test_Search:

    def test_search(self):
        LOGGER.info('eggs info')
        LOGGER.warning('eggs warning')
        LOGGER.error('eggs error')
        LOGGER.critical('eggs critical')
        #search = self.current_page
        #search.do_login()
        pass
