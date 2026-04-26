<script lang="ts">
	import { cva, type VariantProps } from 'class-variance-authority';
	import { cn } from '@/utils/cn';
	import { Button as BitsButton } from 'bits-ui';

	const buttonVariants = cva(
		'inline-flex items-center gap-2 rounded-full font-ui font-medium transition-colors cursor-pointer disabled:cursor-not-allowed disabled:opacity-40 whitespace-nowrap',
		{
			variants: {
				variant: {
					primary: 'bg-pl-accent text-pl-bg hover:bg-pl-accent-h',
					ghost: 'bg-transparent text-pl-ink border border-pl-rule hover:bg-pl-card'
				},
				size: {
					sm: 'px-3.5 py-2 text-[13px]',
					md: 'px-5 py-3 text-[14px]',
					lg: 'px-7 py-4 text-[15px]'
				}
			},
			defaultVariants: {
				variant: 'primary',
				size: 'md'
			}
		}
	);

	type ButtonVariants = VariantProps<typeof buttonVariants>;

	let {
		variant = 'primary',
		size = 'md',
		class: className,
		...restProps
	}: ButtonVariants & BitsButton.RootProps = $props();
</script>

<BitsButton.Root class={cn(buttonVariants({ variant, size }), className)} {...restProps} />
