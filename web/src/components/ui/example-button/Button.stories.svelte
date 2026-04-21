<script module>
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import Button from './Button.svelte';

	const { Story } = defineMeta({
		title: 'UI/Button',
		component: Button,
		tags: ['autodocs'],
		argTypes: {
			variant: {
				control: { type: 'select' },
				options: ['primary', 'ghost', 'secondary']
			},
			disabled: { control: 'boolean' }
		},
		parameters: {
			controls: { include: ['variant', 'disabled'] }
		}
	});
</script>

<Story name="Primary" args={{ variant: 'primary' }}>Button</Story>

<Story name="Ghost" args={{ variant: 'ghost' }}>Button</Story>

<Story name="Secondary" args={{ variant: 'secondary' }}>Button</Story>

<Story name="All Variants">
	<div class="flex flex-wrap items-center gap-3 p-4">
		<Button variant="primary">Button</Button>
		<Button variant="ghost">Button</Button>
		<Button variant="secondary">Button</Button>
	</div>
</Story>
