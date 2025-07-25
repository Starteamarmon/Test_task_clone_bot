from bojango.action import ActionManager
from bojango.core.routing import command


@command('start')
async def start(update, context):
	await ActionManager.redirect('s_start', update, context)