<script lang="ts" generics="T extends string">
	import { RadioGroup } from '@/components/ui/radio-group';

	let {
		models,
		model = $bindable()
	}: {
		models: readonly T[];
		model: T;
	} = $props();

	let items = $derived(models.map((m) => ({ value: m, label: m })));
</script>

<div class="flex flex-row items-center gap-3">
	<span class="text-[14px] tracking-[1.2px] text-s-sub-headline uppercase">模型</span>
	<RadioGroup {items} bind:value={model} />
</div>
