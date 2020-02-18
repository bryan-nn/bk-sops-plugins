# -*- coding: utf-8 -*-

import logging

from django.utils.translation import ugettext_lazy as _

from pipeline.conf import settings
from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component



__group_name__ = _(u"远程自定义原子2(CUS2)")

logger = logging.getLogger('celery')

class Pause2Service(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        logger.info('log from Pause2Service')
        return True
        

    def outputs_format(self):
        return []


class Pause2Component(Component):
    name = _(u'远程测试2')
    code = 'pause2_node'
    bound_service = Pause2Service
    form = """
    (function(){
    $.atoms.pause2_node = [
        {
            tag_code: "test_radio",
            type: "radio",
            attrs: {
                name: gettext("测试RADIO"),
                items: [
                    {value: "1", name: "选项1"},
                    {value: "2", name: "选项2"},
                    {value: "3", name: "选项3"},
                ],
                default: "2",
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "test_testarea",
            type: "textarea",
            attrs: {
                name: gettext("测试文本框"),
                placeholder: gettext("提示"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ],
                default: "2",
            }
        },
        {
            tag_code: "test_input",
            type: "input",
            attrs: {
                name: gettext("通天塔"),
                placeholder: gettext("可为空"),
                hookable: true
            },
        },
    ]
})();
    """