from behave import *

use_step_matcher("re")


@when("I press the weather button")
def step_impl(context):
    # context.browser.find_element_by_id('weather').click()
    pass

@then("the weather for Lisbon is displayed")
def step_impl(context):
    # location = weather.lookup_by_location('dublin')
    # condition = location.condition()
    pass