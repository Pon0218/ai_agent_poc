<script module>
	import { defineMeta } from '@storybook/addon-svelte-csf';
	import Topbar from './Topbar.svelte';

	const { Story } = defineMeta({
		title: 'UI/Topbar',
		component: Topbar,
		tags: ['autodocs']
	});
</script>

<Story name="Default" />
