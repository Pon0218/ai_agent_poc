<script module>
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import Button from './Button.svelte';

	const { Story } = defineMeta({
		title: 'UI/Button',
		component: Button,
		tags: ['autodocs'],
		argTypes: {
			variant: { control: { type: 'select' }, options: ['primary', 'ghost'] },
			size: { control: { type: 'select' }, options: ['sm', 'md', 'lg'] },
			disabled: { control: 'boolean' }
		},
		parameters: { controls: { include: ['variant', 'size', 'disabled'] } }
	});
</script>

<Story name="Primary" args={{ variant: 'primary', size: 'md' }}>Analyze →</Story>

<Story name="Ghost" args={{ variant: 'ghost', size: 'md' }}>Get Started</Story>

<Story name="All Variants">
	<div class="flex flex-wrap items-center gap-3 bg-pl-bg p-6">
		<Button variant="primary" size="sm">Small →</Button>
		<Button variant="primary" size="md">Medium →</Button>
		<Button variant="primary" size="lg">Large →</Button>
		<Button variant="ghost" size="sm">Ghost</Button>
		<Button variant="ghost" size="md">Ghost</Button>
	</div>
</Story>
