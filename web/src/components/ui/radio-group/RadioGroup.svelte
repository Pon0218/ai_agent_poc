<script lang="ts">
	import { RadioGroup, type WithoutChildrenOrChild } from 'bits-ui';
	import { cva, type VariantProps } from 'class-variance-authority';
	import { cn } from '@/utils/cn';

	const itemVariants = cva(
		'min-w-21 cursor-pointer rounded px-3 py-2 text-[12px] text-s-sub-headline transition-opacity hover:opacity-75',
		{
			variants: {
				variant: {
					card: 'border border-s-card-background data-[state=checked]:bg-s-card-background'
				}
			},
			defaultVariants: {
				variant: 'card'
			}
		}
	);

	type ItemVariants = VariantProps<typeof itemVariants>;

	type Item = { value: string; label: string; disabled?: boolean };

	type Props = WithoutChildrenOrChild<RadioGroup.RootProps> &
		ItemVariants & {
			items: Item[];
		};

	let {
		value = $bindable(''),
		ref = $bindable(null),
		variant = 'card',
		class: className,
		items,
		...restProps
	}: Props = $props();
</script>

<RadioGroup.Root
	bind:value
	bind:ref
	orientation="horizontal"
	class={cn('flex items-center gap-3', className)}
	{...restProps}
>
	{#each items as item (item.value)}
		<RadioGroup.Item
			value={item.value}
			disabled={item.disabled}
			class={itemVariants({ variant })}
		>
			{item.label}
		</RadioGroup.Item>
	{/each}
</RadioGroup.Root>
