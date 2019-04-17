# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.firefox.accounts import FirefoxAccountsPage


# test Firefox state
@pytest.mark.skip_if_not_firefox(reason='Firefox users do not see download buttons')
@pytest.mark.nondestructive
def test_download_buttons_displayed(base_url, selenium):
    page = FirefoxAccountsPage(selenium, base_url).open()
    assert page.is_primary_create_account_button_displayed
    assert page.is_send_tabs_create_account_button_displayed
    assert page.is_sync_create_account_button_displayed
    assert page.is_secondary_create_account_form_displayed
    assert not page.send_tabs_download_button.is_displayed
    assert not page.sync_download_button.is_displayed
    assert not page.secondary_download_button.is_displayed


# test non-Firefox state
@pytest.mark.skip_if_firefox(reason='Non-Firefox users do not see create account buttons')
@pytest.mark.nondestructive
def test_accounts_buttons_displayed(base_url, selenium):
    page = FirefoxAccountsPage(selenium, base_url).open()
    assert page.send_tabs_download_button.is_displayed
    assert page.sync_download_button.is_displayed
    assert page.secondary_download_button.is_displayed
    assert not page.is_primary_create_account_button_displayed
    assert not page.is_send_tabs_create_account_button_displayed
    assert not page.is_sync_create_account_button_displayed
    assert not page.is_secondary_create_account_form_displayed
