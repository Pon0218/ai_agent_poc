<script lang="ts" generics="T extends { label: string }">
	import Button from '@/components/ui/button/Button.svelte';

	let {
		examples,
		onselect
	}: {
		examples: T[];
		onselect: (ex: T) => void;
	} = $props();
</script>

<div class="flex flex-row items-center gap-3">
	<span class="text-[14px] tracking-[1.2px] text-s-sub-headline uppercase">範例</span>
	{#each examples as ex (ex.label)}
		<Button variant="secondary" onclick={() => onselect(ex)}>
			{ex.label}
		</Button>
	{/each}
</div>
