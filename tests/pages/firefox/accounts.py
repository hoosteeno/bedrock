# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.firefox.base import FirefoxBasePage
from pages.regions.download_button import DownloadButton


class FirefoxAccountsPage(FirefoxBasePage):

    URL_TEMPLATE = '/{locale}/firefox/accounts/'

    _primary_create_account_button_locator = (By.ID, 'features-hero-account')
    _send_tabs_download_button_locator = (By.ID, 'send-tabs-download')
    _send_tabs_create_account_button_locator = (By.ID, 'send-tabs-create-account-button')
    _sync_download_button_locator = (By.ID, 'sync-download')
    _sync_create_account_button_locator = (By.ID, 'sync-create-account-button')
    _secondary_download_button_locator = (By.ID, 'accounts-bottom')
    _secondary_create_account_form_locator = (By.ID, 'fxa-email-form')

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.seed_url in s.current_url)
        el = self.find_element(By.TAG_NAME, 'body')
        self.wait.until(lambda s: 'state-fxa-default' not in el.get_attribute('class'))
        return self

    @property
    def is_primary_create_account_button_displayed(self):
        return self.is_element_displayed(*self._primary_create_account_button_locator)

    @property
    def send_tabs_download_button(self):
        el = self.find_element(*self._send_tabs_download_button_locator)
        return DownloadButton(self, root=el)

    @property
    def sync_download_button(self):
        el = self.find_element(*self._sync_download_button_locator)
        return DownloadButton(self, root=el)

    @property
    def secondary_download_button(self):
        el = self.find_element(*self._secondary_download_button_locator)
        return DownloadButton(self, root=el)

    @property
    def is_send_tabs_create_account_button_displayed(self):
        return self.is_element_displayed(*self._send_tabs_create_account_button_locator)

    @property
    def is_sync_create_account_button_displayed(self):
        return self.is_element_displayed(*self._sync_create_account_button_locator)

    @property
    def is_secondary_create_account_form_displayed(self):
        return self.is_element_displayed(*self._secondary_create_account_form_locator)
