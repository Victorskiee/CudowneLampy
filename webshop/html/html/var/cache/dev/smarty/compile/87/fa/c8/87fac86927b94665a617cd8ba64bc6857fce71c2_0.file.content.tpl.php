<?php
/* Smarty version 3.1.39, created on 2021-11-10 02:19:30
  from '/var/www/html/admin776jdno0g/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_618b1e22555a74_13996569',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '87fac86927b94665a617cd8ba64bc6857fce71c2' => 
    array (
      0 => '/var/www/html/admin776jdno0g/themes/default/template/content.tpl',
      1 => 1636055972,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_618b1e22555a74_13996569 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
