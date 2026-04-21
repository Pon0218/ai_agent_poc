<script module>
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import RadioGroup from './RadioGroup.svelte';

	const { Story } = defineMeta({
		title: 'UI/RadioGroup',
		component: RadioGroup,
		tags: ['autodocs'],
		argTypes: {
			variant: { control: { type: 'select' }, options: ['card'] },
			disabled: { control: 'boolean' }
		},
		parameters: {
			controls: { include: ['variant', 'disabled'] }
		}
	});
</script>

<Story
	name="Language"
	args={{
		value: 'zh',
		items: [
			{ value: 'zh', label: '中文 zh' },
			{ value: 'en', label: 'English en' }
		]
	}}
/>

<Story
	name="Model"
	args={{
		value: 'gpt-4.1',
		items: [{ value: 'gpt-4.1', label: 'gpt-4.1' }]
	}}
/>

<Story
	name="Disabled"
	args={{
		value: 'zh',
		disabled: true,
		items: [
			{ value: 'zh', label: '中文 zh' },
			{ value: 'en', label: 'English en' }
		]
	}}
/>
